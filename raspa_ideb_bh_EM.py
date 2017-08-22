#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Captura o IDEB das escolas de Belo Horizonte
@author: neylson
"""

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

url_start = 'http://idebescola.inep.gov.br/ideb/consulta-publica'

browser = webdriver.Firefox()
browser.get(url_start)
select = Select(browser.find_element_by_id('pkCodEstado'))
select.select_by_value('31')
select = Select(browser.find_element_by_id('pkCodMunicipio'))
select.select_by_value('3106200')
browser.find_element_by_id('btnSearch').click()
time.sleep(6)
titulos = browser.find_elements_by_xpath('//table[@class="table-listar-escola"]//th')
dados = browser.find_elements_by_xpath('//table[@class="table-listar-escola"]//td')

#segue construindo os clicadores