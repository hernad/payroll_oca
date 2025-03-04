# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Payroll Contract Advantages OCA",
    "version": "14.0.2.0.0",
    "category": "Human Resources",
    "website": "https://github.com/OCA/payroll",
    "summary": "Allow to define contract advantages for employees.",
    "license": "LGPL-3",
    "author": "Nimarosa, Odoo Community Association (OCA)",
    "depends": ["hr_contract", "payroll"],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_contract_advantage_views.xml",
        "views/hr_contract_views.xml",
    ],
    "application": True,
    "maintainers": ["nimarosa"],
}
