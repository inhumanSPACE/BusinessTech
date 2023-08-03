from django.conf.urls import url
from m3.actions import ActionController
from objectpack import desktop

from .actions import ContentTypePack, GroupPack, PermissionPack, UserPack
from .controller import controller

dict_controller = ActionController(url="/test", name="Работай заебал")


def register_urlpatterns():
    """
    Регистрация конфигурации урлов для приложения
    """
    return [url(*controller.urlpattern)]


def register_actions():
    """
    Регистрация экшен-паков
    """
    return controller.packs.extend(
        [
            GroupPack(),
            PermissionPack(),
            UserPack(),
            ContentTypePack(),
        ]
    )


def register_desktop_menu():
    """
    регистрация элементов рабочего стола
    """
    desktop.uificate_the_controller(
        controller, menu_root=desktop.MainMenu.SubMenu("Demo")
    )
