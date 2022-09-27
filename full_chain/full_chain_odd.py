#!/usr/bin/env python3
import pathlib, acts, acts.examples
from acts.examples.simulation import (
    addParticleGun,
    MomentumConfig,
    EtaConfig,
    ParticleConfig,
    addFatras,
    addDigitization,
)
from acts.examples.reconstruction import (
    addSeeding,
    addCKFTracks,
    CKFPerformanceConfig,
    addVertexFitting,
    VertexFinder,
    TrackSelectorRanges,
)
from common import getOpenDataDetectorDirectory
from acts.examples.odd import getOpenDataDetector

u = acts.UnitConstants
geoDir = getOpenDataDetectorDirectory()
outputDir = pathlib.Path.cwd() / "odd_output"
outputDirCsv = outputDir / "csv"

outputDir.mkdir(parents=True, exist_ok=True)
outputDirCsv.mkdir(parents=True, exist_ok=True)

oddMaterialMap = geoDir / "data/odd-material-maps.root"
oddDigiConfig = geoDir / "config/odd-digi-smearing-config.json"
oddSeedingSel = geoDir / "config/odd-seeding-config.json"
oddMaterialDeco = acts.IMaterialDecorator.fromFile(oddMaterialMap)

detector, trackingGeometry, decorators = getOpenDataDetector(
    geoDir, mdecorator=oddMaterialDeco
)
field = acts.ConstantBField(acts.Vector3(0.0, 0.0, 2.0 * u.T))
rnd = acts.examples.RandomNumbers(seed=42)

s = acts.examples.Sequencer(events=1000, numThreads=-1, outputDir=str(outputDir))

addParticleGun(
    s,
    MomentumConfig(1.0 * u.GeV, 10.0 * u.GeV, transverse=True),
    EtaConfig(-3.0, 3.0, uniform=True),
    ParticleConfig(2, acts.PdgParticle.eMuon, randomizeCharge=True),
    rnd=rnd,
    outputDirRoot=outputDir,
    outputDirCsv=outputDirCsv,
)

addFatras(
    s,
    trackingGeometry,
    field,
    rnd=rnd,
    outputDirRoot=outputDir,
    outputDirCsv=outputDirCsv,
)

addDigitization(
    s,
    trackingGeometry,
    field,
    digiConfigFile=oddDigiConfig,
    rnd=rnd,
    outputDirRoot=outputDir,
    outputDirCsv=outputDirCsv,
)

addSeeding(
    s,
    trackingGeometry,
    field,
    geoSelectionConfigFile=oddSeedingSel,
    outputDirRoot=outputDir,
)

addCKFTracks(
    s,
    trackingGeometry,
    field,
    CKFPerformanceConfig(ptMin=1.0 * u.GeV, nMeasurementsMin=6),
    outputDirRoot=outputDir,
    outputDirCsv=outputDirCsv,
)

addVertexFitting(
    s,
    field,
    TrackSelectorRanges(pt=(1.0 * u.GeV, None), absEta=(None, 3.0), removeNeutral=True),
    vertexFinder=VertexFinder.Iterative,
    trajectories="trajectories",
    outputDirRoot=outputDir,
)

s.run()
