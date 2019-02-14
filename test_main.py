import modules.InputModule_lxc
import modules.Alert_module
import modules.AiModule
import modules.UserInterface_module
import modules.Storage

def test_func():
    main()

def main():
    #input
    pathbo='./example/examplebo.txt'
    pathbp='./example/examplebp.txt'
    pathpul='./example/examplepul.txt'
    bo=modules.InputModule_lxc.input(pathbo)
    bp=modules.InputModule_lxc.input(pathbp)
    pul=modules.InputModule_lxc.input(pathpul)

    #storage
    mstorage = modules.Storage.Storage(bo,bp,pul)

    #ai
    ai = modules.AiModule.AiModule()
    ai.input_check(bo, bp, pul)
    predBloodOxygen, predBloodPressure, prePulse = ai.predict()

    #alert
    alt = modules.Alert_module.Alert()
    for k in range(len(bo)):
        boi = bo[k], 0
        bpi = bp[k], 1
        puli = pul[k], 2
        alt.Alert_for_three_categories_input(boi)
        alt.Alert_for_three_categories_input(bpi)
        alt.Alert_for_three_categories_input(puli)
        alt.Alert_Output()

    #user interface
    modules.UserInterface_module.userinterface_input(mstorage,predBloodOxygen,predBloodPressure,prePulse)
    modules.UserInterface_module.userinterface_output()


if __name__ == "__main__":
    main()
