from rest_framework.permissions import BasePermission

# has_permission работает к неско-м объектам. применяется когда нужно либо создание проверить на что-то, либо лист(create, list)
# has_object_permission -работа с одним объектом (retrieve, update, destroy)

class IsAuthor(BasePermission):

    def has_object_permission(self, request, view, obj):    #есть доступ к запросу, к самому обьекту и здесь мы проверяем
        return request.user.is_authenticated and obj.author == request.user   #если юзер залогинен и автор
