from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Reader(models.Model):
    class Meta:
        db_table = 'readers'
        verbose_name = 'reader'
        verbose_name_plural = 'readers'

    first_name = models.CharField(blank=False, null=False, max_length=58, verbose_name='First name')
    last_name = models.CharField(blank=False, null=False, max_length=50, verbose_name='Last name')
    birthday = models.DateField(blank=True, null=True, verbose_name='Birthday')

    def __str__(self):
        return self.last_name + ' ' + self.first_name


class ReaderPhone(models.Model):
    class Meta:
        db_table = 'readers_phone'
        verbose_name = 'reader phone'
        verbose_name_plural = 'reader phones'

    reader = models.ForeignKey(Reader, blank=False, null=False, verbose_name='Reader', on_delete=models.CASCADE)
    phone_number = PhoneNumberField(region='RU')

    is_active = models.BooleanField(default=True, blank=False, null=False, verbose_name='Is active')

    # def __str__(self):
    #     return f'+{str(self.phone_number)}'

class ReaderAddress(models.Model):
    class Meta:
        db_table = 'readers_address'
        verbose_name = 'reader address'
        verbose_name_plural = 'reader addresses'

    reader = models.ForeignKey(Reader, blank=False, null=False,
                               verbose_name='Reader', on_delete=models.CASCADE)

    city_reader = models.CharField(blank=False, null=False,
                                   max_length=15, verbose_name='City')

    street_reader = models.CharField(blank=False, null=False,
                                     max_length=15, verbose_name='Street')

    house_reader = models.CharField(blank=False, null=False,
                                    max_length=15, verbose_name='Number house and number apartments',
                                    help_text='Only number house and number apartments')

    is_active = models.BooleanField(default=True, blank=False,
                                    null=False, verbose_name='Is active')

    def __str__(self):
        return f' Проживает в городе {self.city_reader} на улице {self.street_reader}  {self.house_reader}'


class ReaderTicket(models.Model):
    class Meta:
        db_table = 'readers_ticket'
        verbose_name = 'reader ticket'
        verbose_name_plural = 'reader tickets'

    reader = models.ForeignKey(Reader, blank=False, null=False, verbose_name='Reader', on_delete=models.CASCADE)
    ticket_number = models.CharField(blank=False, null=False, max_length=10, verbose_name='Library card')

    is_active = models.BooleanField(default=True, blank=False, null=False, verbose_name='Is active')
    valid_until = models.DateField(auto_now_add=False,  verbose_name='Valid until')
    def __str__(self):
        return f'{self.ticket_number}'
