from locust import HttpUser, task, TaskSet, between


# locust -f locust_testing/locustfile.py --host=http://localhost:8000

class UserBehavior(TaskSet):

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.logout()

    def get_token(self):
        response = self.client.get("/login/")
        csrftoken = response.cookies['csrftoken']

        return {
            "X-CSRFToken": csrftoken
        }

    def get_username_and_password(self, username='user1', password='user1password'):
        return {
            'username': username,
            'password': password
        }

    def login(self):
        self.client.post('/login/', data=self.get_username_and_password(), headers=self.get_token())

    def logout(self):
        self.client.post('/logout/', data=self.get_username_and_password(), headers=self.get_token())

    @task(2)
    def select_room(self):
        self.client.get('/select_chat/')

    @task(3)
    def enter_room(self, room_name='some_room'):
        self.client.get(f'/chat/{room_name}/')

    # @task(3)
    # def show_sessions(self):
    #     self.client.get('/accounts/profile/sessions')
    #
    # @task(3)
    # def delete_sessions(self, user_session_id='some_session_key'):
    #     self.client.get(f'/accounts/profile/delete_user_session/{user_session_id}/')
    #
    # @task(3)
    # def change_password(self):
    #     data = {
    #         'old_password': 'admin',
    #         'new_password1': 'Admin712313',
    #         'new_password2': 'Admin712313'
    #     }
    #
    #     self.client.post('/accounts/profile/change_password/', data=data, headers=self.get_token())


# ----------------------------------------------------------------------------------------------------------------------


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(5, 9)
