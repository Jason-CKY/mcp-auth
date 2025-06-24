package envoy.authz

import input.attributes.request.http as http_request

# DECODE JWT BEARER TOKEN
token = payload {
    [_, encoded] := split(http_request.headers.authorization, " ")
    [_, payload, _] := io.jwt.decode(encoded)
}

# Define roles and the groups allowed for each role
roles_allowed_groups = {
    "bypass_maintenance": ["admin-group"]
}

# Define a rule to check if the user can assume a role based on their groups
user_can_assume_role[role] {
    # Some user group must be in the allowed groups for the role
    some group
    group = token.groups[_]
    group_allowed = roles_allowed_groups[role][_]
    group == group_allowed
}

# Output the roles the user can assume
resource_access = {role | role := user_can_assume_role[_]}

# POPULATE HEADERS WITH USER INFO
headers["X-User-Id"] = token.user_id
headers["X-User-Email"] = token.user_email
headers["X-Preferred-Username"] = token.preferred_username
headers["X-Full-Name"] = token.full_name
headers["X-Given-Name"] = token.given_name
headers["X-Family-Name"] = token.family_name
headers["X-Resource-Access"] = concat(",", resource_access)
headers["X-Realm-Roles"] = token.realm_roles
headers["X-Groups"] = concat(",", token.groups)

allow := {
    "allowed": true,
    "headers": headers
}
