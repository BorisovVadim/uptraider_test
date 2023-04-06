from django.db import models


class Category(models.Model):
    """Модель для дерева категорий"""

    class Meta:
        """Класс Meta для назначения отображения
        названий полей в административной панели
        """
        verbose_name = 'Menu category'
        verbose_name_plural = 'Menu categories'

    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        """Метод для отображения созданного имени
        категории меню в административной панели
        """
        return self.name


class TreeMenu(models.Model):
    """Класс для дерева меню"""

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'

    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category,
        verbose_name='category',
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    path = models.CharField(verbose_name='path', max_length=255)

    parent = models.ForeignKey(
        'self',
        verbose_name='parent',
        on_delete=models.SET_DEFAULT,
        null=True,
        blank=True,
        default=0
    )

    def __str__(self) -> str:
        """Метод для отображения созданного имени
        категории меню в административной панели
        """
        return self.name
