package repositories

import "yki/src/entities"

type InMemoryMotionRepository struct {
	motion entities.Motion
}

func NewInMemoryMotionRepository() InMemoryMotionRepository {
	motion := entities.Motion{false}
	return InMemoryMotionRepository{motion}
}

func (immr InMemoryMotionRepository) Update(me entities.Motion) (entities.Motion, error)  {
	immr.motion = me
	return immr.motion, nil
}

func (immr InMemoryMotionRepository) Get() entities.Motion {
	return immr.motion
}
