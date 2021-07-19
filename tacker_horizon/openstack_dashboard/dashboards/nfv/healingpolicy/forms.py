# Copyright 2015 Brocade Communications System, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import yaml

from django.forms import ValidationError
from django.utils.translation import ugettext_lazy as _
from oslo_log import log as logging

from horizon import exceptions
from horizon import forms
from horizon import messages

from tacker_horizon.openstack_dashboard import api

LOG = logging.getLogger(__name__)


class CreateHealing(forms.SelfHandlingForm):
    policy_name = forms.CharField(max_length=255, label=_("Policy Name"))
    action_type = forms.ChoiceField(
        label=_('Action Type'),
        required=True,
        choices=[('workflow', _('Work flow')),
                 ('action', _('Action'))],
        widget=forms.Select(
            attrs={'class': 'switchable', 'data-slug': 'template'}))
    action_id = forms.CharField(label=_("ActionID"),
                                required=True)

    def __init__(self, request, *args, **kwargs):
        super(CreateHealing, self).__init__(request, *args, **kwargs)

        # try:
        #     vnfd_list = api.tacker.vnfd_list(request,
        #                                      template_source='onboarded')
        #     available_choices_vnfd = [(vnf['id'], vnf['name']) for vnf in
        #                               vnfd_list]
        # except Exception as e:
        #     available_choices_vnfd = []
        #     msg = _('Failed to retrieve available VNF Catalog names: %s') % e
        #     LOG.error(msg)

        # try:
        #     vim_list = api.tacker.vim_list(request)
        #     available_choices_vims = [(vim['id'], vim['name']) for vim in
        #                               vim_list]

        # except Exception as e:
        #     available_choices_vims = []
        #     msg = _('Failed to retrieve available VIM names: %s') % e
        #     LOG.error(msg)

        # self.fields['vnfd_id'].choices = [('', _('Select a VNF Catalog Name'))
        #                                   ]+available_choices_vnfd
        # self.fields['vim_id'].choices = [('',
        #                                   _('Select a VIM Name'))
        #                                  ]+available_choices_vims

    # def clean(self):
    #     data = super(CreateHealing, self).clean()

    #     template_file = data.get('template_file', None)
    #     template_raw = data.get('template_input', None)

    #     if template_raw and template_file:
    #         raise ValidationError(
    #             _("Cannot specify both file and direct input."))

    #     if template_file and not template_file.name.endswith('.yaml'):
    #         raise ValidationError(
    #             _("Please upload .yaml file only."))

    #     if template_file:
    #         data['vnfd_template'] = yaml.load(template_file,
    #                                           Loader=yaml.SafeLoader)
    #     elif template_raw:
    #         data['vnfd_template'] = yaml.load(data['template_input'],
    #                                           Loader=yaml.SafeLoader)
    #     else:
    #         data['vnfd_template'] = None

    #     param_file = data.get('param_file', None)
    #     param_raw = data.get('direct_input', None)

    #     if param_raw and param_file:
    #         raise ValidationError(
    #             _("Cannot specify both file and direct input."))

    #     if param_file and not param_file.name.endswith('.yaml'):
    #         raise ValidationError(
    #             _("Please upload .yaml file only."))

    #     if param_file:
    #         data['param_values'] = self.files['param_file'].read()
    #     elif param_raw:
    #         data['param_values'] = data['direct_input']
    #     else:
    #         data['param_values'] = None

    #     config_file = data.get('config_file', None)
    #     config_raw = data.get('config_input', None)

    #     if config_file and config_raw:
    #         raise ValidationError(
    #             _("Cannot specify both file and direct input."))

    #     if config_file and not config_file.name.endswith('.yaml'):
    #         raise ValidationError(_("Only .yaml file uploads supported"))

    #     if config_file:
    #         data['config_values'] = self.files['config_file'].read()
    #     elif config_raw:
    #         data['config_values'] = data['config_input']
    #     else:
    #         data['config_values'] = None

    #     return data

    def handle(self, request, data):
        try:
            policy_name = data['policy_name']
            action_type = data.get('action_type')
            action_id = data.get('action_id')
            healing_arg = {'healing': {'policy_name': policy_name,
                               'action_type': action_type,
                               'action_id': action_id}}
            api.tacker.create_healing(request, healing_arg)
            messages.success(request,
                             _('Healing policy create operation initiated.'))
            return True
        except Exception:
            exceptions.handle(request,
                              _('Failed to create VNF.'))
