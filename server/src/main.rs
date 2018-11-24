extern crate cpal;
// extern crate winapi;

fn main() {
    // println!("Input device:\n {:?}", cpal::default_device(winapi::um::mmdeviceapi::EDataFlow.eRender));
    // println!("Default input device:\n {:?}", cpal::default_input_device().map(|e| e.name()));
    // println!("Default output device:\n {:?}", cpal::default_output_device().map(|e| e.name()));

    let devices = cpal::devices();
    for (device_index, device) in devices.enumerate() {
        println!("{}. \"{}\"", device_index + 1, device.name());
    }
}