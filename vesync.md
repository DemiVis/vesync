https://github.com/markperdue/pyvesync

Look into Home Assistant?
https://www.home-assistant.io/

CESAHR <bash-2018> python3
>>> from pyvesync import VeSync
>>> manager = VeSync("darthveder19@gmail.com","MunOrBust17")
>>> manager.login()
>>> print("\n".join(str(manager.outlets).split(",")))
[DevClass: VeSyncOutlet7A
 Name:Christmas Tree
 Device No: None
 DevStatus: off
 CID: ef18b6d5-0ea6-415f-b4fc-03b2ade4f631
 DevClass: VeSyncOutlet7A
  Name:outlet 3
  Device No: None
        DevStatus: off
         CID: 302e54d8-72e8-473c-ba0a-6e29e0d3879f
          DevClass: VeSyncOutlet7A
           Name:CESAHR
            Device No: None
             DevStatus: on
              CID: 6b31e04b-58cc-4772-ba1a-b84e13fb87af
               DevClass: VeSyncOutlet7A
                Name:Upstairs A/C
                 Device No: None
                  DevStatus: off
                   CID: e50b92fa-0518-4c86-86d4-22d5524c9804
                    DevClass: VeSyncOutlet15A
                     Name:Chill Mode
                      Device No: None
                       DevStatus: off
                        CID: 0LRVsAiGx45df0BckZlHm4BI6RvKNJD1]
                        
                        # outlet off
                         >>> manager.outlets[4].display()
                          Device Name:... Chill Mode     
                           Model: ........ ESW15-USA      
                            Subdevice No: . None           
                             Status: ....... off            
                              Online: ....... online         
                               Type: ......... wifi-switch    
                                CID: .......... 0LRVsAiGx45df0BckZlHm4BI6RvKNJD1
                                 UUID: ......... 02ebdda2-cc3a-45c7-ae95-5e93cf54a2a8
                                  Active Time : . 753  minutes
                                   Energy: ....... 1.3054  kWh
                                    Power: ........ 0.0  Watts
                                     Voltage: ...... 0.0  Volts
                                      Energy Week: .. 5.448  kWh
                                       Energy Month: . 5.448  kWh
                                        Energy Year: .. 100.499  kWh
                                        
                                        ## Outlet on, and want updated data 
                                         >>> manager.update()
                                         >>> manager.update_energy()
                                         >>> manager.outlets[4].display()
                                         Device Name:... Chill Mode     
                                         Model: ........ ESW15-USA      
                                         Subdevice No: . None           
                                         Status: ....... on             
                                         Online: ....... online         
                                         Type: ......... wifi-switch    
                                         CID: .......... 0LRVsAiGx45df0BckZlHm4BI6RvKNJD1
                                         UUID: ......... 02ebdda2-cc3a-45c7-ae95-5e93cf54a2a8
                                         Active Time : . 0  minutes
                                         Energy: ....... 0.0  kWh
                                         Power: ........ 138.4  Watts
                                         Voltage: ...... 119.35  Volts
                                         Energy Week: .. 5.448  kWh
                                         Energy Month: . 5.448  kWh
                                         Energy Year: .. 100.499  kWh
