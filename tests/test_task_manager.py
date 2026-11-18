import unittest

from task_manager import add_task, complete_task, delete_task


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.tasks = []

    def test_add_task(self):
        task = add_task(self.tasks, "Study Git")
        self.assertEqual(len(self.tasks), 1)
        self.assertEqual(task["title"], "Study Git")
        self.assertFalse(task["completed"])

    def test_complete_task(self):
        task = add_task(self.tasks, "Write report")
        self.assertTrue(complete_task(self.tasks, task["id"]))
        self.assertTrue(self.tasks[0]["completed"])

    def test_delete_task(self):
        task = add_task(self.tasks, "Old task")
        self.assertTrue(delete_task(self.tasks, task["id"]))
        self.assertEqual(self.tasks, [])

    def test_empty_title_is_rejected(self):
        with self.assertRaises(ValueError):
            add_task(self.tasks, "   ")

    def test_delete_with_invalid_id(self):
        self.assertFalse(delete_task(self.tasks, 99))


if __name__ == "__main__":
    unittest.main()
