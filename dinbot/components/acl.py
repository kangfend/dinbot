#!/usr/bin/env python
from pyaib.components import component_class


@component_class("acl")
class ACL(object):
    def __init__(self, context, config):
        self.permissions = config.get("permissions", {})

    def allowed(self, trigger, chan, nick):
        channel = self.permissions.get(chan, {})
        cmd = channel.get(trigger, {})

        denied_nicks = set(cmd.get("deny", []))
        if any([(nick in denied_nicks), ('*' in denied_nicks)]):
            return False

        allowed_nicks = set(cmd.get("allow", []))
        if any([(nick in allowed_nicks), ('*' in allowed_nicks)]):
            return True

        return False if cmd else True
