from .models import Queue

def generate_queue_number():
    last = Queue.objects.all().order_by("queue_number").last()

    if not last:
        return 1

    return last.queue_number + 1