# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpnext-adelsdorf"
app_title = "ERPNext Adelsdorf"
app_publisher = "K&K Software AG"
app_description = "This creates ERPNext Adelsdorf"
app_icon = "octicon octicon-beaker"
app_color = "grey"
app_email = "teamx@kk-software.de"
app_license = "MIT"

#fixtures = [{"dt":"DocType", "filters": [["name", "in", ("Wiedervorlagen")]]}]
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = ["/assets/css/erpnext-adelsdorf.min.css"]
# app_include_js = "/assets/magic_frappe/js/magic_frappe.js"

# include js, css files in header of web template
# web_include_js = "/assets/magic_frappe/js/magic_frappe.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "magic_frappe.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "magic_frappe.install.before_install"
# after_install = "magic_frappe.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "magic_frappe.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"magic_frappe.tasks.all"
# 	],
# 	"daily": [
# 		"magic_frappe.tasks.daily"
# 	],
# 	"hourly": [
# 		"magic_frappe.tasks.hourly"
# 	],
# 	"weekly": [
# 		"magic_frappe.tasks.weekly"
# 	]
# 	"monthly": [
# 		"magic_frappe.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "magic_frappe.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "magic_frappe.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "magic_frappe.task.get_dashboard_data"
# }