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

from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from oslo_log import log as logging
from oslo_serialization import jsonutils

from horizon import exceptions
from horizon import forms
from horizon import tabs
from horizon.utils import memoized

from tacker_horizon.openstack_dashboard import api as tacker_api
from tacker_horizon.openstack_dashboard.dashboards.nfv.healingpolicy \
    import forms as project_forms

from tacker_horizon.openstack_dashboard.dashboards.nfv.healingpolicy \
    import tabs as nfv_tabs

LOG = logging.getLogger(__name__)


class IndexView(tabs.TabbedTableView):
    # A very simple class-based view...
    tab_group_class = nfv_tabs.HealingManagerTabs 
    template_name = 'nfv/healingpolicy/index.html'

    def get_data(self, request, context, *args, **kwargs):
        # Add data to the context here...
        return context

class CreateHealingView(forms.ModalFormView):
    form_class = project_forms.CreateHealing
    template_name = 'nfv/healingpolicy/create_healing.html'
    success_url = reverse_lazy("horizon:nfv:healingpolicy:index")
    modal_id = "add_service_modal"
    modal_header = _("Create healing")
    submit_label = _("Create Healing")
    submit_url = "horizon:nfv:healingpolicy:createhealing"

    def get_context_data(self, **kwargs):
        context = super(CreateHealingView, self).get_context_data(**kwargs)
        context['submit_url'] = reverse(self.submit_url)
        return context
