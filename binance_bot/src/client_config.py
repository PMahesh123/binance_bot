# src/client_config.py

class MockClient:
    def futures_create_order(self, **kwargs):
        return {
            "mock": True,
            "order": kwargs,
            "status": "FILLED",
            "message": "This is a simulated order."
        }

def get_client(api_key, api_secret):
    return MockClient()  # Return mock client instead of real one
