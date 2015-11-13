from ROOT import TFile, TBrowser

f = TFile("test_data/events.root")
t = f.Get("events")
nEvents = t.GetEntries()
print 'Number of events = '+ str(nEvents)

# xrange(n) = 0,1,2,...,n-1
for iEv in xrange(nEvents):
    t.GetEntry(iEv)
    nParticles = t.nPart
    print 'Number of particle = ' + str(nParticles)

