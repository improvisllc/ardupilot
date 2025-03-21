#pragma once

#include "AP_RangeFinder_config.h"

#if AP_RANGEFINDER_TRI2C_ENABLED

#include "AP_RangeFinder.h"
#include "AP_RangeFinder_Backend.h"

#include <AP_HAL/I2CDevice.h>

class AP_RangeFinder_TeraRangerI2C : public AP_RangeFinder_Backend
{
public:
    // static detection function
    static AP_RangeFinder_Backend *detect(RangeFinder::RangeFinder_State &_state,
                                          AP_RangeFinder_Params &_params,
                                          AP_HAL::I2CDevice *i2c_dev);

    // update state
    void update(void) override;

protected:

    virtual MAV_DISTANCE_SENSOR _get_mav_distance_sensor_type() const override {
        return MAV_DISTANCE_SENSOR_LASER;
    }

private:
    // constructor
    AP_RangeFinder_TeraRangerI2C(RangeFinder::RangeFinder_State &_state,
    								AP_RangeFinder_Params &_params,
                                 AP_HAL::I2CDevice *i2c_dev);

    bool measure(void);
    bool collect_raw(uint16_t &raw_distance);
    bool process_raw_measure(uint16_t raw_distance, uint16_t &distance_cm);

    bool init(void);
    void timer(void);
    AP_HAL::I2CDevice *dev;

    struct {
        uint32_t sum;
        uint32_t count;
    } accum;
};

#endif  // AP_RANGEFINDER_TRI2C_ENABLED
