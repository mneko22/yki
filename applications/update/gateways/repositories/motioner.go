package repositories

import "yki/src/entities"

type Motioner interface {
	Update(m entities.Motion) (entities.Motion, error)
	Get() entities.Motion
}
