package controllers

import "yki/src/entities"
import "yki/src/usecases"
import "yki/src/gateways/repositories"

type MotionController struct {
	MotionRepository repositories.Motioner
}

func NewMotionController(mr repositories.Motioner) *MotionController {
	return &MotionController{mr}
}

func (mc *MotionController) Get() entities.Motion {
	return mc.MotionRepository.Get()
}

func (mc *MotionController) Update(m entities.Motion) (entities.Motion, error) {
	// TODO:: errorハンドリング
	return usecases.UpdateMotion(m, mc.MotionRepository)
}

func (mc *MotionController) ConverToMotion(status bool) entities.Motion {
	return entities.Motion{status}
}
