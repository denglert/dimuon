#
# Plot dimuon mass distribution for SWC HEP 2015
#
from ROOT import TFile, TBrowser, TH1D


file_events = TFile("test_data/events.root")
tree = file_events.Get("events")
nEvents = tree.GetEntries()
print 'Number of events = '+ str(nEvents)

# xrange(n) = 0,1,2,...,n-1
#for iEv in xrange(nEvents):
#    tree.GetEntry(iEv)
#    nParticles = tree.nPart
#    print 'Number of particle = ' + str(nParticles)

hist_dimuon_mass_nBins = 100
hist_dimuon_mass_massMin = 0
hist_dimuon_mass_massMax = 500

h = TH1D("histo_dimuon_mass","di-muon mass spectrum;m [GeV^{2}/c];Entries", hist_dimuon_mass_nBins, hist_dimuon_mass_massMin, hist_dimuon_mass_massMax )
h.Draw()
#raw_input("Press return to exit.")
