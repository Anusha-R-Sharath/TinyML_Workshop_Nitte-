/*
 * MPU6050.h
 *
 *  Created on: Jul 29, 2026
 *      Author: ADMIN
 */

#ifndef INC_MPU6050_H_
#define INC_MPU6050_H_

#define MPU6050_ADDR 0xD0 //This is left shift 1 bit value of device address 0x68
#define MPU6050_PWR_MGMT_1 0x6B

#define MPU6050_ACCEL_XOUT_H 0x3B //Each one 16 bit address with H and L values
#define MPU6050_ACCEL_YOUT_H 0x3D
#define MPU6050_ACCEL_ZOUT_H 0x3F

#define MPU6050_TEMP_OUT_H 0x41

#define MPU6050_GYRO_XOUT_H 0x43
#define MPU6050_GYRO_YOUT_H 0x45
#define MPU6050_GYRO_ZOUT_H 0x47

void MPU6050_Init (void);
void MPU6050_Read_Accel(void);
void MPU6050_Read_Gyro(void);

float Ax, Ay, Az;
float Gx, Gy, Gz;
extern I2C_HandleTypeDef hi2c1;

void MPU6050_Init() //to wake up MPU6050 IMU sensor
{
	uint8_t Data;
	Data = 0x00;
	HAL_I2C_Mem_Write(&hi2c1, MPU6050_ADDR, MPU6050_PWR_MGMT_1, 1, &Data, sizeof(Data), HAL_MAX_DELAY);
}

void MPU6050_Read_Accel(void)
{
	uint8_t Rec_Data[6];
	uint16_t Accel_X_RAW;
	uint16_t Accel_Y_RAW;
	uint16_t Accel_Z_RAW;


	HAL_I2C_Mem_Read(&hi2c1, MPU6050_ADDR, MPU6050_ACCEL_XOUT_H, 1, Rec_Data, 6, HAL_MAX_DELAY); //6 bytes of data to be received, address size is 1 byte

	Accel_X_RAW = (int16_t)((Rec_Data[0] << 8)| Rec_Data [1]);
	Accel_Y_RAW = (int16_t)((Rec_Data[2] << 8) | Rec_Data [3]);
	Accel_Z_RAW = (int16_t)((Rec_Data[4] << 8) | Rec_Data [5]);

	Ax = Accel_X_RAW/16384; //16384 to get the +/- 2 sensitivity
	Ay = Accel_Y_RAW/16384;
	Az = Accel_Z_RAW/16384;
}

void MPU6050_Read_Gyro(void)
{
	uint8_t Rec_Data[6];
	uint16_t Gyro_X_RAW;
	uint16_t Gyro_Y_RAW;
	uint16_t Gyro_Z_RAW;
	HAL_I2C_Mem_Read(&hi2c1, MPU6050_ADDR, MPU6050_ACCEL_XOUT_H, 1, Rec_Data, 6, HAL_MAX_DELAY); //6 bytes of data to be received, address size is 1 byte

	Gyro_X_RAW = (int16_t)((Rec_Data[0] << 8)| Rec_Data [1]);
	Gyro_Y_RAW = (int16_t)((Rec_Data[2] << 8) | Rec_Data [3]);
	Gyro_Z_RAW = (int16_t)((Rec_Data[4] << 8) | Rec_Data [5]);

	Gx = Gyro_X_RAW/131.0; //131 for sensitivity
	Gy = Gyro_Y_RAW/131.0;
	Gz = Gyro_Z_RAW/131.0;
}

#endif /* INC_MPU6050_H_ */


