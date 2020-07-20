from rest_framework.pagination import PageNumberPagination


class XSResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20


class SMResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 80


class MDResultsSetPagination(PageNumberPagination):
    page_size = 80
    page_size_query_param = 'page_size'
    max_page_size = 200


class LGResultsSetPagination(PageNumberPagination):
    page_size = 200
    page_size_query_param = 'page_size'
    max_page_size = 500
