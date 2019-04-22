from django.db import models

# Create your models here.


class UserBase(models.Model):
    name = models.CharField('姓名', max_length=20)
    phone = models.CharField('手机号', max_length=20)
    id_number = models.CharField('身份证号', max_length=30, unique=True)
    credit_score = models.CharField('同盾信用分', max_length=20)
    final_score = models.CharField('租赁分', max_length=20)
    final_decision = models.CharField('同盾决策结果', max_length=20)
    guard_id = models.CharField('保镖ID', max_length=60, null=True)

    def __str__(self):
        return self.name


class RiskItem(models.Model):
    user_id = models.ForeignKey(UserBase, on_delete=models.CASCADE, verbose_name='用户id')
    score = models.CharField('分数', max_length=20)
    risk_name = models.CharField('风险名', max_length=40)
    decision = models.CharField('决策结果', max_length=20)

    def __str__(self):
        return self.risk_name


class RiskDetail(models.Model):
    risk_item_id = models.ForeignKey(RiskItem, on_delete=models.CASCADE, verbose_name='risk_item_id')
    hit_type_display_name = models.CharField('命中类型显示名', max_length=80, blank=True, null=True)
    fraud_type_display_name = models.CharField('诈骗类型显示名', max_length=80, blank=True, null=True)
    description = models.CharField('描述', max_length=50)
    type = models.CharField('类型', max_length=30)
    platform_count = models.CharField('平台借贷数量', max_length=20, blank=True, null=True)

    def __str__(self):
        return self.hit_type_display_name


class GreyListDetail(models.Model):
    risk_detail_id = models.ForeignKey(RiskDetail, on_delete=models.CASCADE, verbose_name='risk_detail_id')
    evidence_time = models.CharField('证据时间', max_length=40)
    risk_level = models.CharField('风险登记', max_length=20)
    fraud_type = models.CharField('诈骗类型', max_length=30)
    fraud_type_display_name = models.CharField('诈骗类型显示名', max_length=30)
    type = models.CharField('类型', max_length=80, null=True)

    def __str__(self):
        return self.fraud_type_display_name


class PlatformDetail(models.Model):
    risk_detail_id = models.ForeignKey(RiskDetail, on_delete=models.CASCADE, verbose_name='risk_detail_id')
    industry_display_name = models.CharField('行业显示名', max_length=30)
    count = models.CharField('数量', max_length=20)
    type = models.CharField('类型', max_length=80, null=True)

    def __str__(self):
        return self.industry_display_name


class FrequencyDetail(models.Model):
    risk_detail_id = models.ForeignKey(RiskDetail, on_delete=models.CASCADE, verbose_name='risk_detail_id')
    detail = models.CharField('细节内容', max_length=80)
    type = models.CharField('类型', max_length=80)
