register(REPORT,
id    = 'ListeEclair',
name  = _("Liste Eclair"),
description =  _("Produit une liste eclair"),
version = '1.0',
gramps_target_version = '3.4',
include_in_listing = False,
status = STABLE,
fname = 'ListeEclair.py',
authors = ["Eric Doutreleau"],
authors_email = ["eric@doutreleau.fr"],
category = CATEGORY_TEXT,
require_active = False,
reportclass = 'ListeEclairReport',
optionclass = 'ListeEclairOptions',
report_modes = [REPORT_MODE_GUI, REPORT_MODE_CLI]
)
