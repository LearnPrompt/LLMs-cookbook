import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('process_data', ROOT / 'gpt3.5/1_process.py')
process_data = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(process_data)


class FineTuneDataTests(unittest.TestCase):
    def convert(self, system_prompt=None):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'input.jsonl'
            target = Path(directory) / 'output.jsonl'
            rows = [{'questions': f'问题 {i}', 'answers': f'回答 {i}'} for i in range(100)]
            source.write_text(''.join(json.dumps(row, ensure_ascii=False) + '\n' for row in rows), encoding='utf-8')
            process_data.transform_jsonl(source, target, system_prompt)
            result = [json.loads(line)['messages'] for line in target.read_text(encoding='utf-8').splitlines()]
        self.assertEqual(len(result), 100)
        self.assertEqual({(m[-2]['content'], m[-1]['content']) for m in result},
                         {(r['questions'], r['answers']) for r in rows})
        return result

    def test_default_preserves_qa_without_unrelated_instruction(self):
        for messages in self.convert():
            self.assertEqual([m['role'] for m in messages], ['user', 'assistant'])

    def test_explicit_instruction_is_added_to_each_example(self):
        for messages in self.convert('请简洁回答问题。'):
            self.assertEqual(messages[0], {'role': 'system', 'content': '请简洁回答问题。'})
            self.assertEqual([m['role'] for m in messages], ['system', 'user', 'assistant'])

    def test_checked_in_examples_have_no_typo_instruction(self):
        rows = [json.loads(line) for line in (ROOT / 'gpt3.5/output.jsonl').read_text(encoding='utf-8').splitlines()]
        self.assertEqual(len(rows), 100)
        for row in rows:
            self.assertEqual([m['role'] for m in row['messages']], ['user', 'assistant'])


if __name__ == '__main__':
    unittest.main()
