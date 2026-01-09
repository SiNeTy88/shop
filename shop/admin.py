from django.contrib import admin
from .models import Product, Transaction, Role, Users

# Реєструємо модель Товарів з налаштуваннями
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Які колонки показувати в списку
    list_display = ('name', 'price', 'quantity', 'created_at')
    
    # По яких полях можна шукати
    search_fields = ('name',)
    
    # Фільтри збоку (дуже зручно)
    list_filter = ('created_at',)
    
    # Можливість редагувати ціну прямо в списку (без заходу всередину)
    list_editable = ('price', 'quantity')

# Реєструємо модель Транзакцій
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    
    # Це додає красивий віджет для вибору багатьох товарів (M2M)
    # Замість простого списку буде два вікна "Доступні" -> "Вибрані"
    filter_horizontal = ('items',) 
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role',)
# Просто реєструємо інші моделі без особливих налаштувань

admin.site.register(Users)