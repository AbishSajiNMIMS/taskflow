from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Task


class TaskFlowTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="alice", password="correct-horse")
        self.other_user = User.objects.create_user(username="bob", password="correct-battery")

    def test_anonymous_user_is_redirected_to_login(self):
        response = self.client.get(reverse("task_list"))
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('task_list')}")

    def test_user_can_create_and_view_own_task(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse("task_list"), {
            "title": "Write tests", "priority": "high", "due_date": "2026-10-01",
        })
        self.assertRedirects(response, reverse("task_list"))
        task = Task.objects.get()
        self.assertEqual(task.owner, self.user)
        self.assertEqual(task.due_date, date(2026, 10, 1))
        self.assertContains(self.client.get(reverse("task_list")), "Write tests")

    def test_task_actions_are_owner_scoped(self):
        task = Task.objects.create(owner=self.other_user, title="Private task")
        self.client.force_login(self.user)
        response = self.client.post(reverse("toggle_task", args=[task.id]))
        self.assertEqual(response.status_code, 404)
        response = self.client.post(reverse("delete_task", args=[task.id]))
        self.assertEqual(response.status_code, 404)
        self.assertTrue(Task.objects.filter(pk=task.pk).exists())

    def test_user_can_toggle_and_delete_task(self):
        self.client.force_login(self.user)
        task = Task.objects.create(owner=self.user, title="Ship feature")
        self.assertRedirects(
            self.client.post(reverse("toggle_task", args=[task.id])),
            reverse("task_list"),
        )
        task.refresh_from_db()
        self.assertTrue(task.done)
        self.assertRedirects(
            self.client.post(reverse("delete_task", args=[task.id])),
            reverse("task_list"),
        )
        self.assertFalse(Task.objects.filter(pk=task.id).exists())
