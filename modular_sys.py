import InputModule_lxc
import Alert_module
import AiModule
import UserInterface_module
import storage

def main():
    
    #user interface
    UserInterface_module.userinterface_input()
    UserInterface_module.userinterface_output()

    #input
    pathbo="./examplebo.txt"
    pathbp="./examplebp.txt"
    pathpul="./examplepul.txt"
    bo=InputModule_lxc.input(pathbo)
    bp=InputModule_lxc.input(pathbp)
    pul=InputModule_lxc.input(pathpul)

    #storage
    mstorage = storage.storage(bo,bp,pul)

    #ai
    ai = AiModule.AiModule()
    ai.input_check(bo, bp, pul)
    predBloodOxygen, predBloodPressure, prePulse = ai.predict()

    #alert
    alt = Alert_module.Alert()
    for k in range(len(bo)):
        boi = bo[k], 0
        bpi = bp[k], 1
        puli = pul[k], 2
        alt.Alert_for_three_categories_input(boi)
        alt.Alert_for_three_categories_input(bpi)
        alt.Alert_for_three_categories_input(puli)
        alt.Alert_Output()


if __name__ == "__main__":
    main()
