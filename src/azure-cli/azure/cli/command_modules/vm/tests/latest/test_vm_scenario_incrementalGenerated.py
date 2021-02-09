# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import os
from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer
from .example_steps import step_disk_access_show_private_link_resource
from .example_steps import step_disk_access_delete
from .example_steps import step_gallery_application_create
from .example_steps import step_gallery_application_show
from .example_steps import step_gallery_application_list
from .example_steps import step_gallery_application_version_list
from .example_steps import step_gallery_application_delete
from .example_steps import step_ssh_public_key_create
from .example_steps import step_ssh_public_key_show
from .example_steps import step_ssh_public_key_generate_key_pair
from .example_steps import step_virtual_machine_reimage
from .example_steps import step_virtual_machine_scale_set_vm_extension_create
from .example_steps import step_virtual_machine_scale_set_vm_extension_show
from .example_steps import step_virtual_machine_scale_set_vm_extension_list
from .example_steps import step_virtual_machine_scale
from .. import (
    try_manual,
    raise_if,
    calc_coverage
)


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Env setup_scenario
@try_manual
def setup_scenario(test, rg, rg_2):
    pass


# Env cleanup_scenario
@try_manual
def cleanup_scenario(test, rg, rg_2):
    pass


# Testcase: Scenario
@try_manual
def call_scenario(test, rg, rg_2):
    setup_scenario(test, rg, rg_2)
    step_disk_access_show_private_link_resource(test, rg, rg_2, checks=[])
    step_disk_access_delete(test, rg, rg_2, checks=[])
    step_gallery_application_create(test, rg, rg_2, checks=[
        test.check("location", "West US", case_sensitive=False),
        test.check("description", "This is the gallery application description.", case_sensitive=False),
        test.check("eula", "This is the gallery application EULA.", case_sensitive=False),
        test.check("privacyStatementUri", "myPrivacyStatementUri}}", case_sensitive=False),
        test.check("releaseNoteUri", "myReleaseNoteUri", case_sensitive=False),
        test.check("supportedOSType", "Windows", case_sensitive=False),
        test.check("name", "{myGalleryApplication}", case_sensitive=False),
    ])
    step_gallery_application_show(test, rg, rg_2, checks=[
        test.check("location", "West US", case_sensitive=False),
        test.check("description", "This is the gallery application description.", case_sensitive=False),
        test.check("eula", "This is the gallery application EULA.", case_sensitive=False),
        test.check("privacyStatementUri", "myPrivacyStatementUri}}", case_sensitive=False),
        test.check("releaseNoteUri", "myReleaseNoteUri", case_sensitive=False),
        test.check("supportedOSType", "Windows", case_sensitive=False),
        test.check("name", "{myGalleryApplication}", case_sensitive=False),
    ])
    step_gallery_application_list(test, rg, rg_2, checks=[
        test.check('length(@)', 1),
    ])
    step_gallery_application_version_list(test, rg, rg_2, checks=[])
    step_gallery_application_delete(test, rg, rg_2, checks=[])
    step_ssh_public_key_create(test, rg, rg_2, checks=[
        test.check("location", "westus", case_sensitive=False),
        test.check("publicKey", "{{ssh-rsa public key}}", case_sensitive=False),
        test.check("name", "{mySshPublicKey}", case_sensitive=False),
    ])
    step_ssh_public_key_show(test, rg, rg_2, checks=[
        test.check("location", "westus", case_sensitive=False),
        test.check("publicKey", "{{ssh-rsa public key}}", case_sensitive=False),
        test.check("name", "{mySshPublicKey}", case_sensitive=False),
    ])
    step_ssh_public_key_generate_key_pair(test, rg, rg_2, checks=[])
    step_virtual_machine_reimage(test, rg, rg_2, checks=[])
    step_virtual_machine_scale_set_vm_extension_create(test, rg, rg_2, checks=[])
    step_virtual_machine_scale_set_vm_extension_show(test, rg, rg_2, checks=[])
    step_virtual_machine_scale_set_vm_extension_list(test, rg, rg_2, checks=[])
    step_virtual_machine_scale(test, rg, rg_2, checks=[])
    cleanup_scenario(test, rg, rg_2)


# Test class for Scenario
@try_manual
class VmScenarioTest(ScenarioTest):

    def __init__(self, *args, **kwargs):
        super(VmScenarioTest, self).__init__(*args, **kwargs)
        self.kwargs.update({
            'mySshPublicKey': 'mySshPublicKeyName',
            'myDiskAccess': 'myDiskAccess',
            'myGalleryApplication': 'myGalleryApplicationName',
        })


    @ResourceGroupPreparer(name_prefix='clitestvm_myResourceGroup'[:7], key='rg', parameter_name='rg')
    @ResourceGroupPreparer(name_prefix='clitestvm_ResourceGroup'[:7], key='rg_2', parameter_name='rg_2')
    def test_vm_Scenario(self, rg, rg_2):
        call_scenario(self, rg, rg_2)
        calc_coverage(__file__)
        raise_if()
