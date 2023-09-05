import schemdraw
from schemdraw import elements as elm
from schemdraw import dsp

def gen_block_diagramm():    
    annColor = '#00B9FF'    
    nue1Color = '#AAFFAA'
    nue2Color = '#FFAAAA'

    with schemdraw.Drawing(show=False) as d:
        d.config(fontsize=12)
        # bit source
        d += (ds := dsp.Box(w=2,h=2)).label('Digitale \n Daten-\nquelle').fill(nue1Color)
        d += (l1 := elm.lines.Line()).at(ds.E).right().length(1)
        d += (a1 := elm.lines.Annotate()).at(l1.center).to((l1.center[0],l1.center[1]-1)).color(annColor).label('Bits')
        # source coding
        d += (sc := dsp.Box(w=2,h=2)).label('Quellen-\ncodierung').at(l1.end).linestyle('--').fill(nue1Color)
        d += (l2 := elm.lines.Line()).at(sc.E).right().length(1)
        d += (a2 := elm.lines.Annotate()).at(l2.center).to((l2.center[0],l2.center[1]-1)).color(annColor).label('Bits')
        # channel coding
        d += (cc := dsp.Box(w=2,h=2)).label('Kanal-\ncodierung').at(l2.end).linestyle('--').fill(nue2Color)
        d += (l3 := elm.lines.Line()).at(cc.E).right().length(1)
        d += (a3 := elm.lines.Annotate()).at(l3.center).to((l3.center[0],l3.center[1]-1)).color(annColor).label('Bits')
        # line coding
        d += (lc := dsp.Box(w=2,h=2)).label('Leitungs-\ncodierung').at(l3.end).linestyle('--').fill(nue1Color)
        d += (l4 := elm.lines.Line()).at(lc.E).right().length(1)
        d += (a4 := elm.lines.Annotate()).at(l4.center).to((l4.center[0],l4.center[1]-1)).color(annColor).label('Bits')
        # mapper
        d += (ma := dsp.Ic(pins=[dsp.IcPin(side='L'), dsp.IcPin(side='R'), dsp.IcPin(side='R')],
                            size=(2,2), leadlen=0.0).anchor('inL1').label('Mapper')).at(l4.end).fill(nue1Color)
        d += (l5 := elm.lines.Line()).at(ma.inR1).right().length(1).linestyle('--')
        d += (l6 := elm.lines.Line()).at(ma.inR2).right().length(1)
        d += (a5 := elm.lines.Annotate()).at(l5.center).to((l5.center[0],l5.center[1]-1)).color(annColor).label('(komplexe)\n digitale \n Symbole / Bits')
        # pulseforming
        d += (pf := dsp.Ic(pins=[dsp.IcPin(side='L'), dsp.IcPin(side='L'), dsp.IcPin(side='R'), dsp.IcPin(side='R')],
                            size=(2,2), leadlen=0.0).anchor('inL1').label('Puls-\nformung / \n DSP')).at(l5.end).fill(nue1Color)
        d += (l7 := elm.lines.Line()).at(pf.inR1).right().length(1).linestyle('--')
        d += (l8 := elm.lines.Line()).at(pf.inR2).right().length(1)
        d += (a6 := elm.lines.Annotate()).at(l7.center).to((l7.center[0],l7.center[1]-1)).color(annColor).label('(komplexes)\n digitales \n Signal')
        # DAC
        d += (dac := dsp.Ic(pins=[dsp.IcPin(side='L'), dsp.IcPin(side='L'), dsp.IcPin(side='R'), dsp.IcPin(side='R'),dsp.IcPin(side='T')],
                            size=(2,2), leadlen=0.0).anchor('inL1').label('Digital-\nAnalog-\nKonverter')).at(l7.end).fill(nue1Color)
        d += (l9 := elm.lines.Line()).at(dac.inR1).right().length(1).linestyle('--')
        d += (l10 := elm.lines.Line()).at(dac.inR2).right().length(1)
        d += (a7 := elm.lines.Annotate()).at(l9.center).to((l9.center[0],l9.center[1]-1)).color(annColor).label('(komplexes)\n analoges \n Signal')
        # Modulator
        d += (mod := dsp.Ic(pins=[dsp.IcPin(side='L'), dsp.IcPin(side='L'), dsp.IcPin(side='R'),dsp.IcPin(side='T')],
                            size=(2,2), leadlen=0.0).anchor('inL1').label('Modulator')).at(l9.end).linestyle('--').fill(nue2Color)
        d += (l11 := elm.lines.Line()).at(mod.inR1).right().length(1)
        d += (l12 := elm.lines.Line()).at(l11.end).down().length(2)    
        d += (arr1 := elm.lines.Arc2(arrow='<->',k=0.5)).to(mod.inT1).at(dac.inT1).linestyle('--')
        # Kanal + Filter
        d += (ch := dsp.Box(w=2,h=2)).label('Kanal').at(l12.end).fill(nue1Color)
        d += (l13 := elm.lines.Line()).at(ch.S).down().length(1)
        d += (a9 := elm.lines.Annotate()).at(l13.center).to((l13.center[0]-4,l13.center[1])).color('#00B9FF').label('')
        d += (filt := dsp.Box(w=2,h=2)).label('Filter').at(l13.end).linestyle('--').fill(nue1Color)
        d += (l14 := elm.lines.Line()).at(filt.S).down().length(2)
        d += (l15 := elm.lines.Line()).at(l14.end).left().length(1)
        d += (a8 := elm.lines.Annotate()).at(l11.center).to((l13.center[0]-4,l13.center[1])).color('#00B9FF').label('reelles analoges Signal\n (entweder Basisband- oder Bandpasssignal')
        d += (a10 := elm.lines.Annotate()).at(l15.center).to((l13.center[0]-4,l13.center[1])).color('#00B9FF').label('')
        # Demodulator
        d += (demod := dsp.Ic(pins=[dsp.IcPin(side='R'), dsp.IcPin(side='R'), dsp.IcPin(side='L'), dsp.IcPin(side='T')],
                            size=(2,2), leadlen=0.0).anchor('inL1').label('De-\nmodulator')).at(l15.end).linestyle('--').fill(nue2Color)
        d += (l16 := elm.lines.Line()).at(demod.inR1).left().length(1)
        d += (l17 := elm.lines.Line()).at(demod.inR2).left().length(1).linestyle('--')
        d += (a11 := elm.lines.Annotate()).at(l16.center).to((l16.center[0],l16.center[1]+1)).color(annColor).label('(komplexes)\nanaloges\nSignal')    
        # ADC
        d += (adc := dsp.Ic(pins=[dsp.IcPin(side='R'), dsp.IcPin(side='R'), dsp.IcPin(side='L'), dsp.IcPin(side='L'), dsp.IcPin(side='T')],
                            size=(2,2), leadlen=0.0).anchor('inL2').label('Analog-\nDigital-\nKonverter')).at(l17.end).fill(nue1Color)
        d += (l18 := elm.lines.Line()).at(adc.inR1).left().length(1)
        d += (l19 := elm.lines.Line()).at(adc.inR2).left().length(1).linestyle('--')
        d += (a12 := elm.lines.Annotate()).at(l18.center).to((l18.center[0],l18.center[1]+1)).color(annColor).label('(komplexes)\ndigitales\nSignal')
        d += (arr2 := elm.lines.Arc2(arrow='<->',k=-0.5)).to(demod.inT1).at(adc.inT1).linestyle('--')
        # matched filter
        d += (mf := dsp.Ic(pins=[dsp.IcPin(side='R'), dsp.IcPin(side='R'), dsp.IcPin(side='L'), dsp.IcPin(side='L')],
                            size=(2,2), leadlen=0.0).anchor('inL2').label('(matched) \n filter \n/ Entzerrer/\n DSP')).at(l19.end).fill(nue1Color)
        d += (l20 := elm.lines.Line()).at(mf.inR1).left().length(1)
        d += (l21 := elm.lines.Line()).at(mf.inR2).left().length(1).linestyle('--')
        d += (a13 := elm.lines.Annotate()).at(l20.center).to((l20.center[0],l20.center[1]+1)).color(annColor).label('(komplexes)\ndigitales\nSignal')
        # demapper
        d += (dm := dsp.Ic(pins=[dsp.IcPin(side='R'), dsp.IcPin(side='L'), dsp.IcPin(side='L')],
                            size=(2,2), leadlen=0.0).anchor('inL2').label('De-\nmapper / \n Entscheider')).at(l21.end).fill(nue1Color)
        d += (l22 := elm.lines.Line()).at(dm.inR1).left().length(1)    
        d += (a14 := elm.lines.Annotate()).at(l22.center).to((l22.center[0],l22.center[1]+1)).color(annColor).label('Bits')
        # line decoding
        d += (ld := dsp.Box(w=2,h=2)).label('Leitungs-\nde-\ncodierung').at(l22.end).linestyle('--').fill(nue1Color)
        d += (l23 := elm.lines.Line()).at(ld.W).left().length(1)    
        d += (a15 := elm.lines.Annotate()).at(l23.center).to((l23.center[0],l23.center[1]+1)).color(annColor).label('Bits').fill(nue1Color)
        # channel decoding
        d += (cd := dsp.Box(w=2,h=2)).label('Kanal-\nde-\ncodierung').at(l23.end).linestyle('--').fill(nue2Color)
        d += (l24 := elm.lines.Line()).at(cd.W).left().length(1)    
        d += (a16 := elm.lines.Annotate()).at(l24.center).to((l24.center[0],l24.center[1]+1)).color(annColor).label('Bits')
        # source decoding
        d += (sd := dsp.Box(w=2,h=2)).label('Quellen-\nde-\ncodierung').at(l24.end).linestyle('--').fill(nue1Color)
        d += (l25 := elm.lines.Line()).at(sd.W).left().length(1)    
        d += (a17 := elm.lines.Annotate()).at(l25.center).to((l25.center[0],l25.center[1]+1)).color(annColor).label('Bits')
        # sink
        d += (dsk := dsp.Box(w=2,h=2)).label('Digitale\nDaten-\nsenke').at(l25.end).fill(nue1Color)
        
        return d
        #d.save(r'.\images\nue1_overview.svg')