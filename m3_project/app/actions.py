from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from m3_ext.ui.fields import ExtStringField
from objectpack.actions import ObjectPack
from objectpack.ui import BaseEditWindow, ModelEditWindow

from .controller import controller, observer


class GroupPack(ObjectPack):
    url = "/group"
    model = Group
    controller = controller
    add_window = edit_window = ModelEditWindow.fabricate(
        model=model,
        model_register=observer,
    )
    add_to_menu = True
    add_to_desktop = True


class PermissionPack(ObjectPack):
    url = "/permission"
    model = Permission
    controller = controller
    add_window = edit_window = ModelEditWindow.fabricate(
        model=model,
        model_register=observer,
    )
    add_to_menu = True
    add_to_desktop = True


class ContentTypePack(ObjectPack):
    url = "/content-type"
    model = ContentType
    controller = controller
    add_window = edit_window = ModelEditWindow.fabricate(
        model=model,
        model_register=observer,
    )
    add_to_menu = True
    add_to_desktop = True


class UserAddWindow(BaseEditWindow):
    def _init_components(self):
        super(UserAddWindow, self)._init_components()

        self.field__username = ExtStringField(
            label="Имя пользователя", name="username", allow_blank=False, anchor="100%"
        )

        self.field__password = ExtStringField(
            label="Пароль", name="password", allow_blank=False, anchor="100%"
        )

        self.field__first_name = ExtStringField(
            label="Имя", name="first_name", allow_blank=False, anchor="100%"
        )

        self.field__last_name = ExtStringField(
            label="Фамилия", name="last_name", allow_blank=False, anchor="100%"
        )

        self.field__email = ExtStringField(
            label="Почта", name="email", allow_blank=False, anchor="100%"
        )

    def _do_layout(self):
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend(
            (
                self.field__username,
                self.field__password,
                self.field__first_name,
                self.field__last_name,
                self.field__email,
            )
        )

    def set_params(self, params):
        super(UserAddWindow, self).set_params(params)
        self.height = "auto"


class UserPack(ObjectPack):
    url = "/user"
    model = User
    controller = controller
    add_window = edit_window = UserAddWindow
    add_to_menu = True
    add_to_desktop = True
    can_delete = True

    columns = [
        {
            "data_index": "username",
            "header": "Имя пользователя",
            "width": 2,
        },
        {
            "data_index": "first_name",
            "header": "Имя",
            "width": 2,
        },
        {
            "data_index": "last_name",
            "header": "Фамилия",
            "width": 2,
        },
        {
            "data_index": "email",
            "header": "Почта",
            "width": 2,
        },
    ]
