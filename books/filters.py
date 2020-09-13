from rest_framework import filters


class MyCustomFilter:


    def filter_queryset(self, request, queryset, view):
        # return queryset.filter(id__gt= 2)  # больше или равно
        return queryset.filter(owner = request.user)

        # return queryset.filter(owner__username=request.user.username)# так делать не нужно не правельно