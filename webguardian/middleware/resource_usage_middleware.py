import psutil
from django.utils.deprecation import MiddlewareMixin

class ResourceUsageMiddleware(MiddlewareMixin):
    def process_request(self, request):
        process = psutil.Process()
        request.cpu_before = process.cpu_percent(interval=None)
        request.memory_before = process.memory_info().rss / (1024 * 1024)  # In MB

    def process_response(self, request, response):
        process = psutil.Process()
        cpu_after = process.cpu_percent(interval=None)
        memory_after = process.memory_info().rss / (1024 * 1024)  # In MB

        print(f"CPU Usage: {cpu_after - request.cpu_before}%")
        print(f"Memory Usage: {memory_after - request.memory_before} MB")

        return response
