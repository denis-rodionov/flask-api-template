class TodoService():
    def __init__(self):
        self.data = [
            {
                'title': "Book a flight to Bali",
                'description': "Find the cheapest and fastest flight in best-flights.net",
                'done': False
            },
            {
                'title': "Pack the luggage",
                'description': "Write a list, pack the things in the suitcase",
                'done': True
            }
        ]

    def get_all(self):
        return self.data

    def add(self, todo_item):
        self.data.append(todo_item)
