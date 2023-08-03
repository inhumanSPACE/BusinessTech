from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
from m3_ext.ui.fields import ExtStringField
from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow, BaseEditWindow

from .controller import observer, controller


class GroupPack(ObjectPack):
    url = '/group'
    model = Group
    controller = controller
    add_window = edit_window = ModelEditWindow.fabricate(
        model=model,
        model_register=observer,
    )
    add_to_menu = True
    add_to_desktop = True


class PermissionPack(ObjectPack):
    url = '/permission'
    model = Permission
    controller = controller
    add_window = edit_window = ModelEditWindow.fabricate(
        model=model,
        model_register=observer,
    )
    add_to_menu = True
    add_to_desktop = True


class ContentTypePack(ObjectPack):
    url = '/test'
    model = ContentType
    controller = controller
    add_window = edit_window = ModelEditWindow.fabricate(
        model=model,
        model_register=observer,
    )
    # add_window = BaseEditWindow()
    add_to_menu = True
    add_to_desktop = True


class UserAddWindow(BaseEditWindow):
    def _init_components(self):
        super(UserAddWindow, self)._init_components()

        self.field__username = ExtStringField(
            label=u'Имя пользователя',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__password = ExtStringField(
            label=u'Пароль',
            name='password',
            allow_blank=False,
            anchor='100%')

        self.field__first_name = ExtStringField(
            label=u'Имя',
            name='first_name',
            allow_blank=False,
            anchor='100%')

        self.field__last_name = ExtStringField(
            label=u'Фамилия',
            name='last_name',
            allow_blank=False,
            anchor='100%')

        self.field__email = ExtStringField(
            label=u'Почта',
            name='email',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__username,
            self.field__password,
            self.field__first_name,
            self.field__last_name,
            self.field__email
        ))

    def set_params(self, params):
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'


class UserPack(ObjectPack):
    url = '/user'
    model = User
    controller = controller
    add_window = edit_window = UserAddWindow
    add_to_menu = True
    add_to_desktop = True
    can_delete = True

    columns = [
        {
            'data_index': 'username',
            'header': u'Имя пользователя',
            'width': 2,
        },
        {
            'data_index': 'first_name',
            'header': u'Имя',
            'width': 2,
        },

        {
            'data_index': 'last_name',
            'header': u'Фамилия',
            'width': 2,
        },
        {
            'data_index': 'email',
            'header': u'Почта',
            'width': 2,
        },
    ]

