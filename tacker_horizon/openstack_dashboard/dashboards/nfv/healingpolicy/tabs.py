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

from django.utils.translation import ugettext_lazy as _
from horizon import exceptions
from horizon import tabs
from horizon import utils as horizon_utils

from tacker_horizon.openstack_dashboard import api
from tacker_horizon.openstack_dashboard.dashboards.nfv import utils
from tacker_horizon.openstack_dashboard.dashboards.nfv.healingpolicy import tables


class HealingPolicyTab(tabs.TableTab):
    name = _("HealingPolicy Tab")
    slug = "healingpolicy_tab"
    table_classes = (tables.HealingManagerTable,)
    template_name = ("horizon/common/_detail_table.html")
    preload = False

    def has_more_data(self, table):
        return self._has_more

    def get_healingpolicy_data(self):
        try:
            instances = []
            hps = api.tacker.healing_list(self.request)

            if len(hps) > horizon_utils.functions.get_page_size(
                    self.request):
                self._has_more = True
            else:
                self._has_more = False

            for hp in hps:
                obj = tables.HealingManagerItem(
                    hp['id'],
                    hp['policy_name'],
                    hp['action_id'],
                    hp['action_type'])
                instances.append(obj)
            return instances
        except Exception:
            self._has_more = False
            error_message = _('Unable to get instances')
            exceptions.handle(self.request, error_message)

            return []


class HealingManagerTabs(tabs.TabGroup):
    slug = "healingpolicy_tabs"
    tabs = (HealingPolicyTab, )
    sticky = True



