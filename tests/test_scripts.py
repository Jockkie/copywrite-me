"""Tests for the scripts that ship with this skill. Run: python -m unittest discover -s tests -v"""
import csv
import importlib.util
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL = "copywrite-me"


def path(*parts):
    return os.path.join(ROOT, "skills", SKILL, *parts)


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, file)
    mod = importlib.util.module_from_spec(spec)
    sys.argv = [file]
    spec.loader.exec_module(mod)
    return mod


def run(*args, stdin=None):
    return subprocess.run([sys.executable, *args], capture_output=True, text=True, input=stdin)


class CopyScore(unittest.TestCase):
    def setUp(self):
        self.m = load("copy_score", path("scripts", "copy_score.py"))

    def test_single_element_section_weighs_less(self):
        card = {"sections": {"Opening": {"Headline or hook": "strong", "Promise": "strong"},
                             "Body": {"Problem in their words": "weak"},
                             "Editing": {"Clarity": "strong", "Flow": "strong", "Tightness": "strong"}}}
        total, weak = self.m.score(card)
        self.assertGreater(total, 70)
        self.assertEqual(weak, [("Body", "Problem in their words")])

    def test_unknown_element_warns(self):
        self.assertTrue(self.m.validate({"sections": {"Body": {"Typo element": "strong"}}}))

class Anonymize(unittest.TestCase):
    def test_dates_kept_phones_masked(self):
        script = path("scripts", "anonymize.py")
        with tempfile.TemporaryDirectory() as t:
            src, out = os.path.join(t, "in.csv"), os.path.join(t, "out.csv")
            with open(src, "w", newline="") as f:
                w = csv.writer(f)
                w.writerow(["klant", "datum", "notitie", "bedrag"])
                w.writerow(["Jan Jansen", "2025-01-10", "bel 06-12345678", "1200.50"])
                w.writerow(["Piet", "10-01-2025 14:30", "+31 10 123 4567 of jan@x.nl", "80"])
            r = run(script, src, out)
            self.assertEqual(r.returncode, 0, r.stderr)
            text = open(out).read()
            self.assertIn("2025-01-10", text)
            self.assertIn("10-01-2025 14:30", text)
            self.assertNotIn("06-12345678", text)
            self.assertNotIn("jan@x.nl", text)
            self.assertNotIn("Jan Jansen", text)

class Hook(unittest.TestCase):
    hook = os.path.join(ROOT, "hooks", "check_reply.py")

    def reply(self, text, tool=None, skill=SKILL, active=False):
        entries = [{"type": "user", "message": {"content": "please use " + SKILL}}]
        if tool:
            entries.append({"type": "assistant", "message": {"content": [{"type": "tool_use", "name": tool, "input": {}}]}})
        entries.append({"type": "assistant", "message": {"content": [{"type": "text", "text": text}]}})
        with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False) as f:
            f.write("\n".join(json.dumps(e) for e in entries))
        r = run(self.hook, skill, stdin=json.dumps({"transcript_path": f.name, "stop_hook_active": active}))
        return r.stdout.strip()

    def test_one_question_passes(self):
        self.assertEqual(self.reply("What type of practice is it?"), "")

    def test_two_questions_block(self):
        self.assertIn("block", self.reply("How many per week? And who makes them?"))

    def test_compound_question_blocks(self):
        self.assertIn("block", self.reply("How many per week, and who makes them?"))

    def test_gap_list_counts_as_one(self):
        self.assertEqual(self.reply("Three quick gaps:\n1. Which channel?\n2. Which date?\n3. Price?"), "")

    def test_quoted_question_ignored(self):
        self.assertEqual(self.reply('She asked "is this right?". What does your week look like?'), "")

    def test_to_whom_compound_blocks(self):
        self.assertIn("block", self.reply("What do you sell, and to whom?"))

    def test_translation_line_ignored(self):
        self.assertEqual(self.reply("Wil je erbij zijn?\nIn English: Want to join?"), "")

    def test_note_to_self_blocks(self):
        self.assertIn("block", self.reply("Note to self: run the script. How many?"))

    def test_false_save_claim_blocks(self):
        self.assertIn("block", self.reply("I added this to business-context.md."))
        self.assertEqual(self.reply("I added this to business-context.md.", tool="Write"), "")

    def test_inactive_skill_and_loop_guard(self):
        self.assertEqual(self.reply("A? B?", skill="some-other-skill"), "")
        self.assertEqual(self.reply("A? B?", active=True), "")


if __name__ == "__main__":
    unittest.main()
