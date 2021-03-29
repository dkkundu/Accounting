from decimal import Decimal as D

from django.db import models
from django.conf import settings
from django.urls import reverse





class Organization(models.Model):
    display_name = models.CharField(max_length=150,
        help_text="Name that you communicate")
    legal_name = models.CharField(max_length=150,
        help_text="Official name to appear on your reports, sales "
                  "invoices and bills")

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name="owned_organizations",
                              on_delete=models.CASCADE)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name="organizations",
                                     blank=True, null=True)

    class Meta:
        pass

    def __str__(self):
        return self.legal_name

    def get_absolute_url(self):
        return reverse('books:organization-detail', args=[self.pk])

    @property
    def turnover_excl_tax(self):
        return self.invoices.turnover_excl_tax() or D('0.00')

    @property
    def turnover_incl_tax(self):
        return self.invoices.turnover_incl_tax() or D('0.00')

    @property
    def debts_excl_tax(self):
        return self.bills.debts_excl_tax() or D('0.00')

    @property
    def debts_incl_tax(self):
        return self.bills.debts_incl_tax() or D('0.00')

    @property
    def profits(self):
        return self.turnover_excl_tax - self.debts_excl_tax

    @property
    def collected_tax(self):
        return self.turnover_incl_tax - self.turnover_excl_tax

    @property
    def deductible_tax(self):
        return self.debts_incl_tax - self.debts_excl_tax

    @property
    def tax_provisionning(self):
        return self.collected_tax - self.deductible_tax

    @property
    def overdue_total(self):
        due_invoices = self.invoices.dued()
        due_turnonver = due_invoices.turnover_incl_tax()
        total_paid = due_invoices.total_paid()
        return due_turnonver - total_paid

