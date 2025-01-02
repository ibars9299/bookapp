from django.core.cache import cache
from django.conf import settings
import os

class PDFCacheMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        if request.path.startswith('/media/books/pdfs/'):
            pdf_path = request.path.split('/media/')[-1]
            cache_key = f'pdf_{pdf_path}'
            
            if not cache.get(cache_key):
                file_path = os.path.join(settings.MEDIA_ROOT, pdf_path)
                with open(file_path, 'rb') as f:
                    cache.set(cache_key, f.read(), timeout=60*60*24)  # 24 saat
        
        return response 