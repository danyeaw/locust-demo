import json

from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    @task(6)
    def hello(self):
        self.client.get('/')

    @task(10)
    def health(self):
        self.client.get('/health')

    @task(3)
    def shorter(self):
        self.client.get('/shorter')

    @task(1)
    def longer(self):
        response = self.client.get('/longer')
        payload = json.loads(response.content)
        print(payload['results'])


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000