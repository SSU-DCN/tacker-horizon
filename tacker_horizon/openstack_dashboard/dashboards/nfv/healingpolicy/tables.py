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
from django.utils.translation import ungettext_lazy

from horizon import tables

from openstack_dashboard import policy
from tacker_horizon.openstack_dashboard import api



class CreateHealing(tables.LinkAction):
    name = "createhealing"
    verbose_name = _("Create Healing")
    classes = ("ajax-modal",)
    icon = "plus"
    url = "horizon:nfv:healingpolicy:createhealing"


class HealingManagerItem(object):
    def __init__(self, id, name, action_id, action_type):
        self.id = id
        self.name = name
        self.action_id = action_id
        self.action_type = action_type


class HealingManagerTable(tables.DataTable):
    id = tables.Column("id",
                         verbose_name=_("Policy ID"))
    name = tables.Column("name",
                         verbose_name=_("Policy Name"))
    action_id = tables.Column("action_id",
                         verbose_name=_("Action ID"))
    action_type = tables.Column("action_type", verbose_name=_("Action type"))



    class Meta(object):
        name = "healingpolicy"
        verbose_name = _("HealingPolicy")
        table_actions= (CreateHealing,)
