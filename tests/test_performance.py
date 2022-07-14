from locust import FastHttpUser, task


class PyTemplatesUser(FastHttpUser):
    @task
    def test(self):
        self.client.get("whoami")
