from django.urls import path
from .views import generate_fake_data, phone_numbers, ends_with_seven, ends_with_nine_eight_five, all_numbers

urlpatterns = [
    path('', generate_fake_data, name='generate_fake_data'),
    path('phone-numbers/', phone_numbers, name='phone_numbers'),
    path('ends-with-seven/', ends_with_seven, name='ends_with_seven'),
    path('ends-with-nine-eight-five/', ends_with_nine_eight_five, name='ends_with_nine_eight_five'),
    path('all_numbers/', all_numbers, name='all_numbers'),

]