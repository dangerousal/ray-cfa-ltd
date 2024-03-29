# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.
{
    'name': "Job Card",
    'version': '1.0',

     'depends': [
                'project', 
                'stock', 
                'document', 
                'hr',
                'hr_timesheet',
                'material_purchase_requisitions'
                ],
   
    'price': 99.0,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'summary': """Job Card for Worker / Technician / Users / Machine Operator""",
    'description': """
    Job Card
Tags:
Machine Operator
Quality Check list
Wokshop Team
Instruction
Timesheet,
Costsheet,
Material Requisition,
Requisition Line,
Job Invoice Line,

Added Quality Check list on job card.
Added Workshop Team on Job Card.
Added Instruction on Job Card,
Added Timesheet on Job Card,
Added Costsheet on Job Card,
Added Material Requisition on Job Card,
Added Material Requisition Line on Job Card
Added Job Invoice Line on Job Card
Added Timesheet on Job Card,
Job Card PDF Report,
Costsheet PDF Report on Job Card,
Job Card Timesheet
job card
jobcard
job order card
card job
work card
job instruction
job order
factory
machine
jobs
jobs card
worker
technician
employee card
job order cards  
job cost sheet
Odoo Job Costing And Job Cost Sheet (Contracting)
Odoo job cost sheet
job cost sheet odoo
contracting odoo
odoo construction
job costing (Contracting)
odoo job costing (Contracting)
odoo job costing Contracting
job order odoo
work order odoo
job Contracting
job cost sheet
Odoo Job Costing And Job Cost Sheet (Contracting)
Odoo job cost sheet
job cost sheet odoo
contracting odoo
odoo construction
job costing (Contracting)
odoo job costing (Contracting)
odoo job costing Contracting
job order odoo
work order odoo
job Contracting
job costing
job cost Contracting
odoo Contracting
Contracting odoo job
Jobs
Jobs/Configuration
Jobs/Configuration/Job Types
Jobs/Configuration/Stages
Jobs/Job Costs
Jobs/Job Costs/Job Cost Sheets
Jobs/Job Orders
Jobs/Job Orders/Job Notes
Jobs/Job Orders/Job Orders
Jobs/Job Orders/Project Issues
BOQ
Job Costing
Notes
Project Report
Task Report
Jobs/Materials / BOQ 
Jobs/Materials / BOQ /Material Requisitions/ BOQ
Jobs/Materials / BOQ /Materials
Jobs/Projects
Jobs/Projects/Project Budgets
Jobs/Projects/Project Notes
Jobs/Projects/Projects
Jobs/Sub Contractors 
Jobs/Sub Contractors /Sub Contractors
material requision odoo
Contracting
job Contracting
job sheet
job cost Contracting
job cost plan
costing
cost Contracting
subcontracting
Email: contact@probuse.com for more details.
This module provide Construction Management Related Activity.
Construction
Construction Projects
Budgets
Notes
Materials
Material Request For Job Orders
Add Materials
Job Orders
Create Job Orders
Job Order Related Notes
Issues Related Project
Vendors
Vendors / Contractors

Construction Management
Construction Activity
Construction Jobs
Job Order Construction
Job Orders Issues
Job Order Notes
Construction Notes
Job Order Reports
Construction Reports
Job Order Note
Construction app
Construction 

Basic Job Costing
Job Costing Example
job order costing
job order
job orders
Tracking Labor
Tracking Material
Tracking Overhead
overhead
material plan
job overhead
job labor
Job Cost Sheet
Example For Larger Job
Job costing is a method of costing applied in industries where production is measured in terms of completed jobs. Industries where job costing is generally applied are Printing Press. Automobile Garage, Repair workshops, Ship Building, Foundry and other similar manufacturing units which manufacture to customers� specific requirements.

Job costing is a method of costing whereby cost is compiled for a job or work order. The production is against customer�s orders and not for stock. The cost is not related to the unit of production but is a cost for the job, e. g printing of 5000 ledger sheets, repairs of 50 equipment�s, instead of printing one sheet or repair of one equipment.

The elements of cost comprising Prime Cost viz. direct materials, direct labour and direct expenses are charged directly to the jobs concerned, the overhead charged to a job is an apportioned portion of the departmental overhead.
Advantages of Job Order Costing

Features of Job Costing
Enabling Job Costing
Creating Cost Centres for Job Costing
project job cost
project job costing
project job contracting
project job contract
job contract
jobs contract
construction
Construction app
Construction odoo
odoo Construction

""",
    'author': "Probuse Consulting Service Pvt. Ltd.",
    'website': "www.probuse.com",
    'support': 'contact@probuse.com',
    'live_test_url': 'https://youtu.be/PtQnySJDBCk',
    'images': ['static/description/img1.jpg'],
    'category' : 'Project',
    'data':[
        'security/ir.model.access.csv',
        'data/job_card_data.xml',
        'views/job_card_view.xml',
        'views/project_view.xml',
        'views/stock_picking_view.xml',
        'views/quality_checklist_view.xml',
        'views/workshop_position_view.xml',
        'views/menu_view.xml',
        'views/hr_employee_view.xml',
        'views/account_invoice_view.xml',
        'views/material_purchase_requisition_view.xml',
        'views/report_jobcard_costsheet.xml',
        'views/report_jobcard.xml',
        
        'wizard/job_card_report_wizard_view.xml',
        
        'report/report_job_card.xml',
        'report/report_reg.xml',
    ],
    'installable' : True,
    'application' : False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
