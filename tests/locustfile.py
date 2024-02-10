from locust import HttpUser, task


class PhonesListUser(HttpUser):
    @task
    def view_phones(self):
        self.client.get("/api/v1/phones/")
