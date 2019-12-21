package repositories

import "yki/src/entities"

type InMemoryMotionRepository struct {
}

var motion entities.Motion

func NewInMemoryMotionRepository() InMemoryMotionRepository {
	motion = entities.Motion{false}
	return InMemoryMotionRepository{}
}

func (immr InMemoryMotionRepository) Update(me entities.Motion) (entities.Motion, error)  {
	motion = me
	return motion, nil
}

func (immr InMemoryMotionRepository) Get() entities.Motion {
	return motion
}
