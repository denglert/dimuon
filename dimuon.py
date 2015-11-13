from ROOT import TFile, TBrowser

file_events = TFile("test_data/events.root")
tree = file_events.Get("events")
nEvents = tree.GetEntries()
print 'Number of events = '+ str(nEvents)

# xrange(n) = 0,1,2,...,n-1
for iEv in xrange(nEvents):
    tree.GetEntry(iEv)
    nParticles = tree.nPart
    print 'Number of particle = ' + str(nParticles)

