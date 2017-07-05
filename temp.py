'''
this is a sample for calculating joint probability of given values of each node. 
'''
import json
import sys

# add to PYTHONPATH
sys.path.append("")

from libpgm.nodedata import NodeData
from libpgm.graphskeleton import GraphSkeleton
from libpgm.discretebayesiannetwork import DiscreteBayesianNetwork
from libpgm.lgbayesiannetwork import LGBayesianNetwork
from libpgm.hybayesiannetwork import HyBayesianNetwork
from libpgm.dyndiscbayesiannetwork import DynDiscBayesianNetwork
from libpgm.tablecpdfactorization import TableCPDFactorization
from libpgm.sampleaggregator import SampleAggregator
from libpgm.pgmlearner import PGMLearner
def getTableCPD():
    nd = NodeData()
    skel = GraphSkeleton()
    jsonpath=""
    nd.load(jsonpath)
    skel.load(jsonpath)
    bn = DiscreteBayesianNetwork(skel, nd)
    tablecpd=TableCPDFactorization(bn)
    return tablecpd

tcpd=getTableCPD()
print(tcpd.specificquery(dict(A_Sovereign_nears_default_and_no_rescue_package='1',
                              B_Distressed_Eurpoean_banks = '0',
                              C_Distressed_UK_banks = '0', 
                              D_QE2_for_UK = '0', 
                              E_Major_readjustment_of_risk_premia_for_UK_assets = '0',
                              F_Government_rescue_of_bank = '0',
                              G_Restriction_of_credit_to_UK_economy_and_UK_hous_price_fall = '0',
                              H_UK_Coroprate_credit_spreads = '0',
                              K_UK_equity_prices_fall = '0',
                              L_Gilts_prices_rally = '0'),{}))
